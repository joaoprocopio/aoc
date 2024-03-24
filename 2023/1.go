package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"
	"runtime"
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
	path, ok := relative("./1.txt")

	if !ok {
		panic(ok)
	}

	file, err := os.Open(path)

	if err != nil {
		panic(err)
	}

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}
}
