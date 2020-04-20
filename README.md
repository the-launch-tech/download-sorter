# Download Directory Sorter

- Sorted files and directories within downloads folder into categorized directories based on extension.
- Runs every 10 seconds.

### To Run

- Terminal (go to directory): `cd ~/Library/LaunchAgents/`
- Terminal (create/open file): `nano com.<unique-name>.osx.test.plist`
- Nano Editor (add commands):

```
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST 1.0//EN http://www.apple.com/DTDs/PropertyList-1.0.dtd >
  <plist version="1.0">
    <dict>
      <key>Label</key>
      <string>com.<unique-name>.osx.test</string>
      <key>Program</key>
      <string>/<project-location>/<project-filename>.py</string>
      <key>KeepAlive</key>
      <true/>
    </dict>
  </plist>
```

- Nano Editor (end editing): `ctl + x`
- Nano Editor (confirm save): `y`
- Terminal (start process): `launchctl load ~/Library/LaunchAgents/com.bobbob.osx.test.plist`
- Terminal (stop process): `launchctl unload ~/Library/LaunchAgents/com.bobbob.osx.test.plist`
