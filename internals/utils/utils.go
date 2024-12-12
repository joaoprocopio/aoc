package utils

import (
	"errors"
	"path/filepath"
	"runtime"
)

func ExecutableDirname() (string, error) {
	_, file, _, ok := runtime.Caller(0)

	if !ok {
		return "", errors.New("could not get the executable path")
	}

	cwd := filepath.Dir(file)

	return cwd, nil
}

func CheckErr(err error) {
	if err != nil {
		panic(err)
	}
}
