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

	check(err)

	path := filepath.Join(cwd, "./input.txt")
	file, err := os.Open(path)

	check(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		check(err)
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

func check(err error) {
	if err != nil {
		panic(err)
	}
}
