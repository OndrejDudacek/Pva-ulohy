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
  console.log(inputs, outputs);
};

const readInputAndOutput = (input, output) => {
  const inputFileContents = fs.readFileSync(input, "utf8").trim();
  const outputFileContents = fs.readFileSync(output, "utf8").trim();
  return [inputFileContents, outputFileContents];
};

const checkIfCorrect = (output, expectedOutput) => {
  if (output === expectedOutput) {
    console.log(output, "X", expectedOutput, "✅\n________________________\n");
  } else {
    console.log(output, "X", expectedOutput, "❌\n________________________\n");
  }
};

const generateOutput = (message) => {
  return `Posloupnost:\n${message}`;
};

findInputsAndOutputs();
console.log(readInputAndOutput(inputs[0], outputs[0]));