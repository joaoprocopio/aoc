import fs from "fs"
import path from "path"

import { trebuchet } from "."

const to = (filename: string) => path.join(__dirname, filename)

describe("2023 - 1", () => {
  it("should work on mini input", () => {
    const text = fs.readFileSync(to("mini.txt"), { encoding: "utf-8" })
    const splitted = text.split("\n")

    const result = trebuchet(splitted)

    expect(result).toBe(142)
  })

  it("should work on macro input", () => {
    const text = fs.readFileSync(to("macro.txt"), { encoding: "utf-8" })
    const splitted = text.split("\n")

    const result = trebuchet(splitted)

    expect(result).toBe(53386)
  })
})
