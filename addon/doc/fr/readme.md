# StationPlaylist #

* Auteurs: Geoff Shang, Joseph Lee et d'autres contributeurs.
* Télécharger [version stable][1]
* Télécharger [la version de développement][2]
* Download [long-term support version][3] - for Studio 5.20 users
* NVDA compatibility: 2020.3 to 2020.4

This add-on package provides improved usage of StationPlaylist Studio and
other StationPlaylist apps, as well as providing utilities to control Studio
from anywhere. Supported apps include Studio, Creator, Track Tool, VT
Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.

For more information about the add-on, read the [add-on guide][4].

NOTES IMPORTANTES :

* This add-on requires StationPlaylist suite 5.30 (5.20 for 20.09.x-LTS) or
  later.
* Si vous utilisez Windows 8 ou ultérieur, pour une meilleure expérience,
  désactiver le Mode d'atténuation audio.
* Starting from 2018, [changelogs for old add-on releases][5] will be found
  on GitHub. This add-on readme will list changes from version 20.09 (2020)
  onwards.
* While Studio is running, you can save, reload saved settings, or reset
  add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R
  once, or Control+NVDA+R three times, respectively. This is also applicable
  to encoder settings - you can save and reset (not reload) encoder settings
  if using encoders.

## Raccourcis clavier

La plupart d'entre eux fonctionneront dans Studio uniquement sauf indication
contraire.

* Alt+Maj+T depuis la fenêtre de Studio : annonce le temps écoulé pour la
  piste en cours de lecture.
* Contrôle+Alt+T (glissement à deux doigts vers le bas en mode tactile SPL)
  depuis la fenêtre de Studio : annoncer le temps restant pour la piste en
  cours de lecture.
* NVDA+Maj+F12 (glissement à deux doigts vers le haut en mode tactile SPL)
  depuis la fenêtre de Studio: annonce le temps de diffusion tel que 5
  minutes en haut de l'heure. Appuyez deux fois sur cette commande pour
  annoncer les minutes et les secondes jusqu'au début de l'heure.
* Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens
  alarms category in Studio add-on configuration dialog.
* Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces scheduled time for the loaded playlist.
* Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces total playlist duration.
* Alt+NVDA+3 depuis la fenêtre de Studio : Basculer l'explorateur de chariot
  pour apprendre les assignations de chariot.
* Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces when the selected track is scheduled to play.
* Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor:
  Announces rotation and category associated with the loaded playlist.
* Control+NVDA+f from Studio window: Opens a dialog to find a track based on
  artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to
  find backward.
* Alt+NVDA+R depuis la fenêtre de Studio : parcourt les paramètres d'annonce
  du balayage dans la bibliothèque.
* Contrôle+Maj+X depuis la fenêtre de Studio : Parcourt les paramètres du
  minuteur braille.
* Control+Alt+left/right arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track column.
* Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): Move to first/last track column.
* Control+Alt+up/down arrow (while focused on a track in Studio, Creator,
  Remote VT, and Track Tool): Move to previous/next track and announce
  specific columns.
* Control+NVDA+1 through 0 (while focused on a track in Studio, Creator
  (including Playlist Editor), Remote VT, and Track Tool): Announce column
  content for a specified column (first ten columns by default). Pressing
  this command twice will display column information on a browse mode
  window.
* Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote
  VT, and Track Tool): display data for all columns in a track on a browse
  mode window.
* NVDA+V while focused on a track (Studio's playlist viewer only): toggles
  track column announcement between screen order and custom order.
* Alt+NVDA+C while focused on a track (Studio's playlist viewer only):
  announces track comments if any.
* Alt+NVDA+0 depuis la fenêtre de Studio : Ouvre le dialogue de
  configuration de l'extension Studio.
* Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
* Alt+NVDA+- (tiret) depuis la fenêtre de Studio : Envoyez vos commentaires
  au développeur de l'extension en utilisant le client de messagerie par
  défaut.
* Alt+NVDA+F1: Ouvre le dialogue de bienvenue.

## Commandes non assignées

The following commands are not assigned by default; if you wish to assign
them, use Input Gestures dialog to add custom commands. To do so, from
Studio window, open NVDA menu, Preferences, then Input Gestures. Expand
StationPlaylist category, then locate unassigned commands from the list
below and select "Add", then type the gesutre you wish to use.

* Basculement vers la fenêtre SPL Studio depuis n'importe quel programme.
* Couche Contrôleur SPL.
* Annonçant le statut de Studio, comme la lecture de pistes à partir
  d'autres programmes.
* Announcing encoder connection status from any program.
* Couche Assistant SPL depuis SPL Studio.
* Annoncer le temps y compris les secondes depuis SPL Studio.
* Annonce de la température.
* Annonce du titre de la piste suivante si planifié.
* Annonçant le titre de la piste en cours de lecture.
* Marquage de piste en cours pour le début de l'analyse de durée de piste.
* Effectuer des analyses de durée de piste.
* Prendre des instantanés de playlist
* Recherche de texte dans des colonnes spécifiques.
* Trouver des piste avec une durée qui se situe dans un intervalle donné via
  la recherche de l'intervalle de temps.
* Activer ou désactiver les métadonnées en streaming rapidement.

## Additional commands when using encoders

The following commands are available when using encoders:

* F9: connect the selected encoder.
* F10 (SAM encoder only): Disconnect the selected encoder.
* Control+F9: Connect all encoders.
* Control+F10 (SAM encoder only): Disconnect all encoders.
* F11 : Détermine si NVDA bascule vers la fenêtre Studio pour l'encodeur
  sélectionné  si connecté.
* Maj+F11: Détermine si Studio lit la première piste sélectionnée lorsque
  l'encodeur est connecté à un serveur de streaming.
* Contrôle+F11 : Active ou désactive le contrôle en arrière-plan de
  l'encodeur sélectionné.
* Control+F12: opens a dialog to select the encoder you have deleted (to
  realign encoder labels and settings).
* Alt+NVDA+0 and F12: Opens encoder settings dialog to configure options
  such as encoder label.

De plus, les commandes pour visualiser la colonne sont disponibles, y
compris :

* Contrôle+NVDA+1 : Position de l'encodeur.
* Control+NVDA+2: encoder label.
* Contrôle+NVDA+3 depuis l'Encodeur SAM : Format de l'Encodeur.
* Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
* Control+NVDA+4 from SAM Encoder: Encoder connection status.
* Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection
  status.
* Contrôle+NVDA+5 depuis l'Encodeur SAM : Description du statut de la
  connexion.

## Couche Assistant SPL

This layer command set allows you to obtain various status on SPL Studio,
such as whether a track is playing, total duration of all tracks for the
hour and so on. From any SPL Studio window, press the SPL Assistant layer
command, then press one of the keys from the list below (one or more
commands are exclusive to playlist viewer). You can also configure NVDA to
emulate commands from other screen readers.

Les commandes disponibles sont :

* A : Automatisation.
* C (Shift+C in JAWS layout): Title for the currently playing track.
* C (JAWS layout): Toggle cart explorer (playlist viewer only).
* D (R dans la disposition de JAWS) : Durée restante pour la playlist (si un
  message d’erreur est donné, se déplacer vers la visionneuse de playlist et
  puis tapez cette commande).
* E: Metadata streaming status.
* Maj+1 jusqu'à maj+4, maj+0 : Statut de Métadonnées individuelles en
  streaming URLs (0 est pour l'encodeur DSP).
* F : Recherche de piste (visionneuse de playlist uniquement).
* H : Durée de la musique pour la tranche horaire en cours.
* Maj+H : Durée des pistes restantes pour la tranche horaire.
* I (L in JAWS layout): Listener count.
* K : Se déplacer à la piste marquée (visionneuse de playlist uniquement).
* Contrôle+K : Définir la piste en cours comme le marqueur de position de
  piste (visionneuse de playlist uniquement).
* L (Shift+L in JAWS layout): Line in.
* M : Microphone.
* N : Titre pour la piste suivante planifié.
* P : Statut (en cours de lecture ou arrêté).
* Maj+P : Hauteur de la piste actuelle.
* R (Shift+E in JAWS layout): Record to file enabled/disabled.
* Maj+R : Contrôle du balayage de la bibliothèque en cours.
* S : Piste débute (planifié).
* Maj+S : Durée jusqu'à la piste sélectionnée qui va être jouer (piste
  débute dans).
* T : Mode édition/insertion chariot activé/désactivé.
* U: temps de fonctionnement Studio.
* W: Météo et température si configurée.
* Y: Statut de la modification de la playlist.
* F8 : Prendre des instantanés de playlist (nombre de pistes, piste la plus
  longue, etc.).
* Maj+F8 : Demander des transcriptions de playlist dans de nombreux formats.
* F9 : Marquer la piste en cours pour le début de l'analyse de playlist
  (visionneuse de playlist uniquement).
* F10 : Effectuer une analyse de durée de piste (visionneuse de playlist
  uniquement).
* F12 : basculer entre un profil en cours et un profil prédéfini.
* F1: Aide couche.
* Maj+F1 : Ouvre le guide de l'utilisateur en ligne.

## Contrôleur SPL

Le contrôleur SPL est un ensemble de commandes couches que vous pouvez
utiliser pour contrôler SPL Studio de n'importe où. Appuyez sur la commandes
couche Contrôleur SPL, et NVDA dira, "Contrôleur SPL." Appuyez sur une autre
commande pour contrôler divers paramètres Studio comme activer/désactiver un
microphone ou lire la piste suivante.

Les commandes disponibles pour le Contrôleur SPL sont:

* P: Play the next selected track.
* U: Pause or unpause playback.
* S: Stop the track with fade out.
* T: Instant stop.
* M: Turn on microphone.
* Shift+M: Turn off microphone.
* A: Turn on automation.
* Shift+A: Turn off automation.
* L: Turn on line-in input.
* Shift+L: Turn off line-in input.
* R: Remaining time for the currently playing track.
* Shift+R: Library scan progress.
* C: Title and duration of the currently playing track.
* Shift+C: Title and duration of the upcoming track if any.
* E: Encoder connection status.
* I: Listener count.
* Q: Studio status information such as whether a track is playing,
  microphone is on and others.
* Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
* H: Layer help.

## Track and microphone alarms

By default, NVDA will play a beep if five seconds are left in the track
(outro) and/or intro, as well as to hear a beep if microphone has been
active for a while. To configure track and microphone alarms, press
Alt+NVDA+1 to open alarms settings in Studio add-on settings screen. You can
also use this screen to configure if you'll hear a beep, a message or both
when alarms are turned on.

## Chercheur de piste

Si vous souhaitez trouver rapidement une chanson par artiste ou par nom de
chanson, depuis la liste de piste, appuyez sur Contrôle+NVDA+F. Tapez le nom
de l'artiste ou le nom de la chanson. NVDA va vous placer soit à la chanson
Si cell-ci est trouvé ou il affichera une erreur si elle ne trouve pas la
chanson que vous recherchez. Pour trouver une chanson ou un artiste
précédemment entrée, appuyez sur NVDA+F3 ou NVDA+Maj+F3 Pour trouver en
avant ou en arrière.

Remarque: le Chercheur de piste est sensible à la casse.

## Explorateur de Chariot

Selon l'édition, SPL Studio permet d'assigné jusq'à 96 chariots pendant la
lecture. NVDA vous permet d'entendre quel chariot ou jingle est assigné à
ces commandes.

To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the
cart command once will tell you which jingle is assigned to the
command. Pressing the cart command twice will play the jingle. Press
Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information
on cart explorer.

## Analyse de durée de piste

Pour obtenir la longueur pour jouer les pistes sélectionnés, marquer la
piste en cours pour le début de l'analyse de durée de piste (Assistant SPL,
F9), puis appuyer sur Assistant SPL, F10 lorsque vous atteignez la fin de la
sélection.

## Explorateur de Colonnes

By pressing Control+NVDA+1 through 0, you can obtain contents of specific
columns. By default, these are first ten columns for a track item (in
Studio: artist, title, duration, intro, outro, category, year, album, genre,
mood). For playlist editor in Creator and Remote VT client, column data
depends on column order as shown on screen. In Studio, Creator's main track
list, and Track Tool, column slots are preset regardless of column order on
screen and can be configured from add-on settings dialog under columns
explorer category.

## Track column announcement

You can ask NVDA to announce track columns found in Studio's playlist viewer
in the order it appears on screen or using a custom order and/or exclude
certain columns. Press NVDA+V to toggle this behavior while focused on a
track in Studio's playlist viewer. To customize column inclusion and order,
from column announcement settings panel in add-on settings, uncheck
"Announce columns in the order shown on screen" and then customize included
columns and/or column order.

## Instantanés de playlist

Vous pouvez appuyer sur Assistant SPL , F8 étant focalisée sur une playlist
dans Studio pour obtenir diverses statistiques sur une playlist, y compris
le nombre de pistes dans la playlist, la piste la plus longue, les meilleurs
artistes et ainsi de suite.

## Transcriptions de Playlist

En appuyant sur Assistant SPL, Maj+F8 présentera une boîte de dialogue pour
vous permettre de demander des transcriptions de playlist dans de nombreux
formats, y compris dans un format de texte brut, un tableau HTML ou une
liste.

## Boîte de dialogue configuration

Depuis la fenêtre studio, vous pouvez appuyer sur Alt+NVDA+0 pour ouvrir la
boîte de dialogue configuration de l'extension. Sinon, allez dans le menu
préférences de NVDA et sélectionnez l'élément Paramètres SPL Studio. Cette
boîte de dialogue est également utilisé pour gérer les profils de diffusion.

## Broadcast profiles dialog

You can save settings for specific shows into broadcast profiles. These
profiles can be managed via SPL broadcast profiles dialog which can be
accessed by pressing Alt+NVDA+P from Studio window.

## Mode tactile SPL

Si vous utilisez Studio sur un ordinateur possédant un écran tactile
fonctionnant sous Windows 8 ou version ultérieure et NVDA 2012.3 ou version
ultérieure installé, vous pouvez exécuter certaines commandes Studio depuis
un écran tactile. Tout d'abord utiliser une tape à trois doigts pour
basculer en mode SPL, puis utilisez les commandes tactile énumérées
ci-dessus pour exécuter des commandes.

## Version 21.01/20.09.5-LTS

Version 21.01 supports SPL Studio 5.30 and later.

* 21.01: NVDA 2020.3 or later is required.
* 21.01: column header inclusion setting from add-on settings has been
  removed. NVDA's own table column header setting will control column header
  announcements across SPL suite and encoders.
* Added a command to toggle screen versus custom column inclusion and order
  setting (NVDA+V). Note that this command is available only when focused on
  a track in Studio's playlist viewer.
* SPL Assistant and Controller layer help will be presented as a browse mode
  document instead of a dialog.
* NVDA will no longer stop announcing library scan progress if configured to
  announce scan progress while using a braille display.

## Version 20.11.1/20.09.4-LTS

* Initial support for StationPlaylist suite 5.50.
* Improvements to presentation of various add-on dialogs thanks to NVDA
  2020.3 features.

## Version 20.11/20.09.3-LTS

* 20.11: NVDA 2020.1 or later is required.
* 20.11: Resolved more coding style issues and potential bugs with Flake8.
* Fixed various issues with add-on welcome dialog (Alt+NVDA+F1 from Studio),
  including wrong command shown for add-on feedback (Alt+NVDA+Hyphen).
* 20.11: Column presentation format for track and encoder items across
  StationPlaylist suite (including SAM encoder) is now based on
  SysListView32 list item format.
* 20.11: NVDA will now announce column information for tracks throughout SPL
  suite regardless of "report object description" setting in NVDA's object
  presentation settings panel. For best experience, leave this setting on.
* 20.11: In Studio's playlist viewer, custom column order and inclusion
  setting will affect how track columns are presented when using object
  navigation to move between tracks, including current navigator object
  announcement.
* If vertical column announcement is set to a value other than "whichever
  column I'm reviewing", NVDA will no longer announce wrong column data
  after changing column position on screen via mouse.
* improved playlist transcripts (SPL Assistant, Shift+F8) presentation when
  viewing the transcript in HTML table or list format.
* 20.11: In encoders, encoder labels will be announced when performing
  object navigation commands in addition to pressing up or down arrow keys
  to move between encoders.
* In encoders, in addition to Alt+NVDA+number row 0, pressing F12 will also
  open encoder settings dialog for the selected encoder.

## Version 20.10/20.09.2-LTS

* Due to changes to encoder settings file format, installing an older
  version of this add-on after installing this version will cause
  unpredictable behavior.
* It is no longer necessary to restart NVDA with debug logging mode to read
  debug messages from log viewer. You can view debug messages if log level
  is set to "debug" from NVDA's general settings panel.
* In Studio's playlist viewer, NVDA will not include column headers if this
  setting is disabled from add-on settings and custom column order or
  inclusion settings are not defined.
* 20.10: column header inclusion setting from add-on settings is deprecated
  and will be removed in a future release. In the future NVDA's own table
  column header setting will control column header announcements across SPL
  suite and encoders.
* When SPL Studio is minimized to the system tray (notification area), NVDA
  will announce this fact when trying to switch to Studio from other
  programs either through a dedicated command or as a result of an encoder
  connecting.

## Version 20.09-LTS

Version 20.09.x is the last release series to support Studio 5.20 and based
on old technologies, with future releases supporting Studio 5.30 and more
recent NVDA features. Some new features will be backported to 20.09.x if
needed.

* Due to changes in NVDA, --spl-configvolatile command line switch is no
  longer available to make add-on settings read-only. You can emulate this
  by unchecking "Save configuration when exiting NVDA" checkbox from NVDA's
  general settings panel.
* Removed pilot features setting from Advanced settings category under
  add-on settings (Alt+NVDA+0), used to let development snapshot users test
  bleeding-edge code.
* Column navigation commands in Studio are now available in track lists
  found in listener requests, insert tracks and other screens.
* Various column navigation commands will behave like NVDA's own table
  navigation commands. Besides simplifying these commands, it brings
  benefits such as ease of use by low vision users.
* Vertical column navigation (Control+Alt+up/down arrow) commands are now
  available for Creator, playlist editor, Remote VT, and Track Tool.
* Track columns viewer command (Control+NVDA+hyphen) is now available in
  Creator's Playlist Editor and Remote VT.
* Track columns viewer command will respect column order displayed on
  screen.
* In SAM encoders, improved NVDA's responsiveness when pressing Control+F9
  or Control+F10 to connect or disconnect all encoders, respectively. This
  may result in increased verbosity when announcing the selected encoder
  information.
* In SPL and AltaCast encoders, pressing F9 will now connect the selected
  encoder.

## Anciennes versions

S'il vous plaît voir le lien changelog pour les notes de version  pour les
anciennes versions de l'extension.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=spl

[2]: https://addons.nvda-project.org/files/get.php?file=spl-dev

[3]: https://addons.nvda-project.org/files/get.php?file=spl-lts20

[4]: https://github.com/josephsl/stationplaylist/wiki/SPLAddonGuide

[5]: https://github.com/josephsl/stationplaylist/wiki/splchangelog
