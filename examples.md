Adding Text to LibreOffice Writer:

```shell
echo "write text.insertString(document.Text.createTextCursor(), 'Hello world!', 0)" | nc localhost 9999
```

Filling a Cell in LibreOffice Calc:

```shell
echo "calc document.Sheets[0].getCellRangeByName('A1').Value = 42" | nc localhost 9999
```

Changing the Style of a Cell in Calc:

```shell
echo "calc cell = document.Sheets[0].getCellRangeByName('A1'); cell.CellBackColor = 16776960" | nc localhost 9999
```

Adding a New Line with Text in Writer:

```shell
echo "write text.insertControlCharacter(document.Text.createTextCursor(), uno.getConstantByName('com.sun.star.text.ControlCharacter.PARAGRAPH_BREAK'), False); text.insertString(document.Text.createTextCursor(), 'New line of text', 0)" | nc localhost 9999
```

Saving the Current Document:

```shell
echo "write document.store()" | nc localhost 9999
```
