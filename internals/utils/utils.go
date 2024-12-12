package utils

import (
	"bufio"
	"errors"
	"os"
	"path/filepath"
	"runtime"
)

var ErrUnreadable = errors.New("Unreadable file path")

func PanicIfErr(err error) {
	if err != nil {
		panic(err)
	}
}

func ExecutableDirname(skip int) (string, error) {
	_, file, _, ok := runtime.Caller(skip)

	if !ok {
		return "", ErrUnreadable
	}

	cwd := filepath.Dir(file)

	return cwd, nil
}

func FileScanner(relpath string, skip int) (*os.File, *bufio.Scanner, error) {
	excdirname, err := ExecutableDirname(skip)

	if err != nil {
		return nil, nil, err
	}

	fullpath := filepath.Join(excdirname, relpath)
	file, err := os.Open(fullpath)

	if err != nil {
		return nil, nil, err
	}

	scanner := bufio.NewScanner(file)

	return file, scanner, nil
}
