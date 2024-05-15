const fs = require("fs");

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

const sumPairs = (sequence) => {
  let sums = [];
  for (let y = 0; y < sequence.length; y++) {
    let num = sequence[y];
    let toBeSumed = [num];
    for (let i = y + 1; i < sequence.length; i++) {
      toBeSumed.push(sequence[i]);
      sums.push(toBeSumed.reduce((a, b) => a + b));
    }
  }
  return sums;
};

const calculateSumPairs = (sequence) => {
  const sums = sumPairs(sequence);
  const sumCounts = new Map();
  for (let sum of sums) {
    if (sumCounts.has(sum)) {
      sumCounts.set(sum, sumCounts.get(sum) + 1);
    } else {
      sumCounts.set(sum, 1);
    }
  }
  let pairCount = 0;
  for (let count of sumCounts.values()) {
    pairCount += (count * (count - 1)) / 2;
  }
  return pairCount;
};

const checkSequence = (sequence) => {
  for (let num of sequence) if (isNaN(num)) return false;
  if (sequence.length <= 0) return false;
  if (sequence.length > 2000) return false;
  return true;
};

const inputs = [];
const outputs = [];
findInputsAndOutputs();
for (let i in inputs) {
  const inputFile = inputs[i];
  const outputFile = outputs[i];
  const [inputFileContents, outputFileContents] = readInputAndOutput(
    inputFile,
    outputFile
  );
  const sequence = inputFileContents
    .trim()
    .replace("\n", " ")
    .split(" ")
    .map(Number);
  console.log(sequence);
  let pairCount = checkSequence(sequence);
  if (!pairCount) {
    checkIfCorrect(generateOutput("Nespravny vstup."), outputFileContents);
    continue;
  }
  pairCount = calculateSumPairs(sequence);
  checkIfCorrect(
    generateOutput(`Pocet dvojic: ${pairCount}`),
    outputFileContents
  );
}
