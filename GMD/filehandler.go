package main

import(
	"io"
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/dialog"
	"fyne.io/fyne/v2/widget"

	"errors"

)

func OpenFile(windw fyne.Window, textArea *widget.Entry) {
	dialog.ShowFileOpen(func(r fyne.URIReadCloser, err error){
		if err != nil || r == nil{
			return
		}
		defer r.Close()

		data, err := io.ReadAll(r)
		if err !=nil {
			errAlert := errors.New("file could not be loaded")
			dialog.ShowError(errAlert, windw)
		}
		textArea.SetText(string(data))
	} , windw)
}

func SaveFile(windw fyne.Window, textArea *widget.Entry) {
	dialog.ShowFileSave(func(w fyne.URIWriteCloser, err error){
		if err != nil || w == nil{
			return
		}
		defer w.Close()

		_, err = w.Write([]byte(textArea.Text))
		if err !=nil {
			errAlert := errors.New("file could not be saved")
			dialog.ShowError(errAlert, windw)
		}
	} , windw)
}



