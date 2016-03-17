# StationPlaylist Studio update checker
# A support module for SPL add-on
# Copyright 2015-2016, Joseph Lee, released under GPL.

# Provides update check facility, basics borrowed from NVDA Core's update checker class.

import urllib
import os # Essentially, update download is no different than file downloads.
from calendar import month_abbr # Last modified date formatting.
import cPickle
import threading
import gui
import wx
import tones
import time
import addonHandler
import globalVars

# Add-on manifest routine (credit: various add-on authors including Noelia Martinez).
# Do not rely on using absolute path to open to manifest, as installation directory may change in a future NVDA Core version (highly unlikely, but...).
_addonDir = os.path.join(os.path.dirname(__file__), "..", "..")
# Move this to the main app module in case version will be queried by users.
SPLAddonVersion = addonHandler.Addon(_addonDir).manifest['version']
# Cache the file size for the last downloaded SPL add-on installer (stored in hexadecimal for security).
SPLAddonSize = "0x0"
# The Unix time stamp for add-on check time.
SPLAddonCheck = 0
# Update metadata storage.
SPLAddonState = {}
# Update URL (the only way to change it is installing a different version from a different branch).
SPLUpdateURL = "http://addons.nvda-project.org/files/get.php?file=spl-dev"
# 7.0 beta only: Stable version URL and flag.
SPLUpdateURL2 = "http://addons.nvda-project.org/files/get.php?file=spl"
_stableChannel = False
_pendingChannelChange = False
# Update check timer.
_SPLUpdateT = None
# How long it should wait between automatic checks.
_updateInterval = 86400
# Set if a socket error occurs.
_retryAfterFailure = False
# Stores update state.
_updatePickle = os.path.join(globalVars.appArgs.configPath, "splupdate.pickle")

# Come forth, update check routines.
def initialize():
	global SPLAddonState, SPLAddonSize, SPLAddonCheck, _stableChannel
	try:
		SPLAddonState = cPickle.load(file(_updatePickle, "r"))
		SPLAddonCheck = SPLAddonState["PDT"]
		SPLAddonSize = SPLAddonState["PSZ"]
		_stableChannel = "PCH" in SPLAddonState
	except IOError:
		SPLAddonState["PDT"] = 0
		SPLAddonState["PSZ"] = 0x0

def terminate():
	global SPLAddonState
	# Store new values if it is absolutely required.
	stateChanged = SPLAddonState["PSZ"] != SPLAddonSize or SPLAddonState["PDT"] != SPLAddonCheck
	if stateChanged:
		SPLAddonState["PSZ"] = SPLAddonSize
		SPLAddonState["PDT"] = SPLAddonCheck
		cPickle.dump(SPLAddonState, file(_updatePickle, "wb"))
	SPLAddonState = None


def _versionFromURL(url):
	filename = url.split("/")[-1]
	name = filename.split(".nvda-addon")[0]
	return name[name.find("-")+1:]

def _lastModified(lastModified):
	# Add-ons server uses British date format (dd-mm-yyyy).
	day, month, year = lastModified.split()[1:4]
	# Adapted an entry on Stack Overflow on how to convert month names to indecies.
	month = str({v: k for k,v in enumerate(month_abbr)}[month]).zfill(2)
	return "-".join([year, month, day])

# Run the progress thread from another thread because urllib.urlopen blocks everyone.
_progressThread = None

def _updateProgress():
	tones.beep(440, 40)

def updateProgress():
	global _progressThread
	_progressThread = wx.PyTimer(updateProgress)
	_progressThread.Start(1000)

def stopUpdateProgress():
	global _progressThread
	_progressThread.Stop()
	_progressThread = None

# 7.0 beta/LTS: allow custom version to be passed into this function.
def updateQualify(url, cv=None):
	# The add-on version is of the form "major.minor". The "-dev" suffix indicates development release.
	# Anything after "-dev" indicates a try or a custom build.
	# LTS: Support upgrading between LTS releases.
	curVersion =cv if cv is not None else SPLAddonVersion.split("-")[0]
	# Because we'll be using the same file name for snapshots...
	if "-dev" in SPLAddonVersion: curVersion+="-dev"
	size = hex(int(url.info().getheader("Content-Length")))
	version = _versionFromURL(url.url)
	# In case we are running the latest version, check the content length (size).
	if version == curVersion:
		if "-dev" not in version:
			return None
		elif ("-dev" in SPLAddonVersion and size != SPLAddonSize):
			return version
	elif version > curVersion:
		return version
	else:
		return ""

# The update check routine.
# Auto is whether to respond with UI (manual check only), continuous takes in auto update check variable for restarting the timer.
# LTS: The "lts" flag is used to obtain update metadata from somewhere else (typically the LTS server).
def updateCheck(auto=False, continuous=False, lts=False):
	if _pendingChannelChange:
		wx.CallAfter(gui.messageBox, _("Did you recently tell SPL add-on to use a different update channel? If so, please restart NVDA before checking for add-on updates."), _("Update channel changed"), wx.ICON_ERROR)
		return
	global _SPLUpdateT, SPLAddonCheck, _retryAfterFailure
	# Regardless of whether it is an auto check, update the check time.
	# However, this shouldnt' be done if this is a retry after a failed attempt.
	if not _retryAfterFailure: SPLAddonCheck = time.time()
	# Should the timer be set again?
	if continuous and not _retryAfterFailure: _SPLUpdateT.Start(_updateInterval*1000, True)
	# Auto disables UI portion of this function if no updates are pending.
	if not auto: tones.beep(110, 40)
	# All the information will be stored in the URL object, so just close it once the headers are downloaded.
	if not auto:
		threading.Thread(target=updateProgress).start()
	updateCandidate = False
	try:
		# 7.0 beta: give priority to stable version if this is such a case.
		if _stableChannel:
			urlStable = urllib.urlopen(SPLUpdateURL2)
			urlStable.close()
			if urlStable.code == 200 and updateQualify(urlStable, cv="6.a") not in (None, ""):
				url = urllib.urlopen(SPLUpdateURL2)
			else:
				url = urllib.urlopen(SPLUpdateURL)
			url.close()
		else:
			url = urllib.urlopen(SPLUpdateURL)
			url.close()
	except IOError:
		_retryAfterFailure = True
		if not auto:
			stopUpdateProgress()
			# Translators: Error text shown when add-on update check fails.
			wx.CallAfter(gui.messageBox, _("Error checking for update."), _("Check for add-on update"), wx.ICON_ERROR)
		if continuous: _SPLUpdateT.Start(600000, True)
		return
	if _retryAfterFailure:
		_retryAfterFailure = False
		# Now is the time to update the check time if this is a retry.
		SPLAddonCheck = time.time()
	if url.code != 200:
		if auto:
			if continuous: _SPLUpdateT.Start(_updateInterval*1000, True)
			return # No need to interact with the user.
		# Translators: Text shown when update check fails for some odd reason.
		checkMessage = _("Add-on update check failed.")
	else:
		# Am I qualified to update?
		qualified = updateQualify(url, cv ="6.a" if _stableChannel else None)
		if qualified is None:
			if auto:
				if continuous: _SPLUpdateT.Start(_updateInterval*1000, True)
				return
			# Translators: Presented when no add-on update is available.
			checkMessage = _("No add-on update available.")
		elif qualified == "":
			if auto:
				if continuous: _SPLUpdateT.Start(_updateInterval*1000, True)
				return
			# Translators: An error text shown when one is using a newer version of the add-on.
			checkMessage = _("You appear to be running a version newer than the latest released version. Please reinstall the official version to downgrade.")
		else:
			# Translators: Text shown if an add-on update is available.
			checkMessage = _("Studio add-on {newVersion} ({modifiedDate}) is available. Would you like to update?".format(newVersion = qualified, modifiedDate = _lastModified(url.info().getheader("Last-Modified"))))
			updateCandidate = True
	if not auto: stopUpdateProgress()
	# Translators: Title of the add-on update check dialog.
	if not updateCandidate: wx.CallAfter(gui.messageBox, checkMessage, _("Check for add-on update"))
	else: wx.CallAfter(getUpdateResponse, checkMessage, _("Check for add-on update"), url.info().getheader("Content-Length"))

def getUpdateResponse(message, caption, size):
	global SPLAddonSize
	if gui.messageBox(message, caption, wx.YES | wx.NO | wx.CANCEL | wx.CENTER | wx.ICON_QUESTION) == wx.YES:
		SPLAddonSize = hex(int(size))
		os.startfile(SPLUpdateURL)

