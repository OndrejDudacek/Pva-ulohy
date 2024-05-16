const fs = require("fs");

const inputs = [];
const outputs = [];

const findInputsAndOutputs = () => {
  const files = fs.readdirSync(__dirname);
  for (let file of files) {
    if (file.includes("in")) {
      inputs.push(file);
    } else if (file.includes("out")) {
      outputs.push(file);
    }
  }
};

const readInputAndOutput = (input, output) => {
  const inputFileContents = fs.readFileSync(input, "utf8").trim();
  const outputFileContents = fs.readFileSync(output, "utf8").trim();
  return [inputFileContents, outputFileContents];
};

const generateOutput = (message) => {
  return `Posloupnost:\n${message}`;
};

findInputsAndOutputs();
let [input, expectedOutput] = readInputAndOutput(inputs[0], outputs[0]);
input = input.split("\n\n").map((x) => x.split("\n"));
let rack = input.shift();
const racks = [];
let index = null;
for (const item of rack) {
  if (item.includes("#")) {
    if (index !== null) {
      index++;
    } else {
      index = 0;
    }
    racks[index] = [];
  } else {
    racks[index].push(item);
  }
}
for (const item of input) {
    
}