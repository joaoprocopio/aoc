import fs from "fs"
import path from "path"

import { trebuchet } from "."

describe("2023 - 1", () => {
  const miniPath = path.join(__dirname, "mini.txt")
  const macroPath = path.join(__dirname, "macro.txt")

  it("should work on mini input", () => {
    const text = fs.readFileSync(miniPath, { encoding: "utf-8" })
    const splitted = text.split("\n")

    const result = trebuchet(splitted)

    expect(result).toBe(142)
  })

  it("should work on macro input", () => {
    const text = fs.readFileSync(macroPath, { encoding: "utf-8" })
    const splitted = text.split("\n")

    const result = trebuchet(splitted)

    expect(result).toBe(53386)
  })
})
