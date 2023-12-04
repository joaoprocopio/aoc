import fs from "fs"
import path from "path"

import { trebuchet } from "."

const to = (filename: string) => path.join(__dirname, filename)

it("2023 - 1.1 - trebuchet", () => {
  const text = fs.readFileSync(to("input.txt"), { encoding: "utf-8" })
  const splitted = text.split("\n")

  const result = trebuchet(splitted)

  expect(result).toBe(53386)
})
