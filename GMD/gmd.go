package main

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
	"fyne.io/fyne/v2/theme"
)

func main() {
	gmd := app.New()

	editWindow := gmd.NewWindow("File name")

	text := widget.NewMultiLineEntry()
	text.SetPlaceHolder("Type here...")

	editWindow.Resize(fyne.NewSize(650, 650))
	editWindow.ShowAndRun()
}
