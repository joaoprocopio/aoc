package utils

import (
	"errors"
	"fmt"
	"path/filepath"
	"runtime"
)

func ExecutableDirname(skip int) (string, error) {
	_, file, _, ok := runtime.Caller(skip)

	fmt.Println(file)

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
