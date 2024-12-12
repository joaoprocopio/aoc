// https://adventofcode.com/2024/day/1
package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"path/filepath"
	"runtime"
)

func main() {
	cwd, err := getcwd()

	if err != nil {
		panic(err)
	}

	path := filepath.Join(cwd, "./input.txt")
	file, err := os.Open(path)

	if err != nil {
		panic("could not open this file")
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}

func getcwd() (string, error) {
	_, file, _, ok := runtime.Caller(0)

	if !ok {
		return "", errors.New("could not get the executable path")
	}

	cwd := filepath.Dir(file)

	return cwd, nil
}
