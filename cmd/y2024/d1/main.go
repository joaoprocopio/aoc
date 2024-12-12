// https://adventofcode.com/2024/day/1
package main

import (
	"bufio"
	"fmt"
	"os"
	"path/filepath"

	"github.com/joaoprocopio/aoc/internals/utils"
)

func main() {
	cwd, err := utils.ExecutableDirname(1)

	utils.CheckErr(err)

	path := filepath.Join(cwd, "./input.txt")
	file, err := os.Open(path)

	utils.CheckErr(err)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		fmt.Println(scanner.Text())
	}

	if err := scanner.Err(); err != nil {
		utils.CheckErr(err)
	}
}
