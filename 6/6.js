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
