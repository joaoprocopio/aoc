// https://adventofcode.com/2023/day/1
package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"runtime"
	"strconv"
	"unicode"
)

func relative(path string) (string, bool) {
	_, callerPath, _, ok := runtime.Caller(0)

	if !ok {
		return "", ok
	}

	callerDir := filepath.Dir(callerPath)
	relativeFilePath := filepath.Join(callerDir, path)

	return relativeFilePath, ok
}

func main() {
	path, ok := relative("./day1.txt")

	if !ok {
		panic(ok)
	}

	file, err := os.Open(path)

	if err != nil {
		panic(err)
	}

	total := 0
	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()

		first := ""
		last := ""

		for _, char := range line {
			isDigit := unicode.IsDigit(char)

			if !isDigit {
				continue
			}

			value := string(char)

			if first == "" && last == "" {
				first = value
				last = value
			}

			last = value
		}

		integer, err := strconv.Atoi(first + last)

		if err != nil {
			panic(err)
		}

		total += integer
	}

	fmt.Println(total)
}
