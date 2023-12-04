import fs from "fs"
import path from "path"

import { trebuchet } from "."

const file = path.join(__dirname, "input.txt")
const content = fs.readFileSync(file, { encoding: "utf-8" })
const text = content.split("\n")

it("2023 - 1.1 - trebuchet", () => {
  const result = trebuchet(text)

  expect(result).toBe(53386)
})
