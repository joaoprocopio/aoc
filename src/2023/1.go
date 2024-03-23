package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func path(file string) (string, error) {
	dir, err := os.Getwd()

	if err != nil {
		return "", err
	}

	path := filepath.Join(dir, file)

	return path, nil
}

func main() {
	path, err := path("1.txt")

	if err != nil {
		panic(err)
	}

	fmt.Println(path)
}
