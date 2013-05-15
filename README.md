# impressive-presenter
### An HTML presenter screen for Impressive

![](https://dl.dropbox.com/u/1116031/images/impressive-presenter.png)

Based on [Seppe vanden Broucke's code][vandenbroucke].

## Dependencies
* pyPdf

## Usage
This workflow is recommended:

1. Make your PDF slides however you like.
2. Run `impressive-presenter.sh` with your presentation file as an argument. It will create some files in the presentation directory.
3. [Modify the `.info` file][info-scripts] if you need to (for transitions, for example). The `notes` property will be shown on the presenter screen as speaker notes. HTML is allowed.
4. At the time of your presentation, open `presenter.html` in your laptop screen. In Chrome, you'll need to execute the browser with the `--allow-file-access-from-files` flag, otherwise it won't work. This flag could change without notice, so be careful and check the [documentation][chrome-flags]. Or just use another browser.
5. In the main screen, start your presentation with Impressive. If everything goes well, `presenter.html` should update its info.

[vandenbroucke]: http://blog.macuyiko.com/2009/12/buillding-presenter-view-for-linux.html
[info-scripts]: http://impressive.sourceforge.net/manual.php#scripts
[chrome-flags]: http://peter.sh/experiments/chromium-command-line-switches/