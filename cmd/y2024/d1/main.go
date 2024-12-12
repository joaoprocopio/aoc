// https://adventofcode.com/2024/day/1
package main

import (
	"fmt"

	"github.com/joaoprocopio/aoc/internals/utils"
)

func main() {
	file, scanner, err := utils.FileScanner("./sample.txt", 2)
	utils.PanicIfErr(err)
	defer file.Close()

	for scanner.Scan() {
		text := scanner.Text()

		fmt.Println(text, " TEST")
	}

	if err := scanner.Err(); err != nil {
		utils.PanicIfErr(err)
	}
}
