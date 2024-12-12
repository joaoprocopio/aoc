package utils

import (
	"errors"
	"path/filepath"
	"runtime"
)

var ErrUnreadable = errors.New("Unreadable file path")

func ExecutableDirname(skip int) (string, error) {
	_, file, _, ok := runtime.Caller(skip)

	if !ok {
		return "", ErrUnreadable
	}

	cwd := filepath.Dir(file)

	return cwd, nil
}

func CheckErr(err error) {
	if err != nil {
		panic(err)
	}
}
