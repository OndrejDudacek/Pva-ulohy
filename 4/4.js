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
  return inputFileContents, outputFileContents;
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
  console.log(sums);
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
  console.log(sumCounts);
  let pairCount = 0;
  for (let count of sumCounts.values()) {
    pairCount += (count * (count - 1)) / 2;
  }
  return pairCount;
};

const generateOutput = (pairCount) => {
  return `Posloupnost:\nPocet dvojic: ${pairCount}`;
};

const checkOutput = (output, expectedOutput) => {
  if (output === expectedOutput) {
    console.log(output, expectedOutput, "✅\n________________________\n");
  } else {
    console.log(output, expectedOutput, "❌\n________________________\n");
  }
};

findInputsAndOutputs();
for (let i in inputs){
  const inputFile = inputs[i];
  const outputFile = outputs[i];
  const [inputAndOutput] = readInputAndOutput(inputFile, outputFile);
  const input = inputAndOutput.split("\n")[0];
  const expectedOutput = inputAndOutput.split("\n")[1];
  const sequence = input.split(" ").map((num) => parseInt(num));
  const pairCount = calculateSumPairs(sequence);
  const output = generateOutput(pairCount);
  checkOutput(output, expectedOutput);
}

// const readline = require("readline");

// function calculateSumPairs(sequence) {
//   const sumCounts = new Map();
//   const n = sequence.length;

//   // Funkce pro výpočet součtu prvků v poli
//   function calculateSum(arr, start, end) {
//     let sum = 0;
//     for (let i = start; i <= end; i++) {
//       sum += arr[i];
//     }
//     return sum;
//   }

//   // Generování všech možných intervalů a jejich součtů
//   for (let i = 0; i < n; i++) {
//     for (let j = i + 1; j < n; j++) {
//       const sum = calculateSum(sequence, i, j);
//       if (sumCounts.has(sum)) {
//         sumCounts.get(sum).push([i, j]);
//       } else {
//         sumCounts.set(sum, [[i, j]]);
//       }
//     }
//   }

//   // Hledání počtu dvojic intervalů se stejným součtem
//   let pairCount = 0;
//   for (const intervals of sumCounts.values()) {
//     const intervalCount = intervals.length;
//     pairCount += (intervalCount * (intervalCount - 1)) / 2;
//   }

//   return pairCount;
// }

// async function main() {
//   const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout,
//   });

//   let sequence = [];
//   console.log("Zadejte číselnou posloupnost a stiskněte Enter:");
//   for await (const line of rl) {
//     if (line === "") {
//       break;
//     }
//     const num = parseInt(line);
//     if (isNaN(num)) {
//       console.log("Chybný vstup. Zadejte platné celé číslo.");
//       continue;
//     }
//     sequence.push(num);
//   }

//   if (sequence.length === 0) {
//     console.log("Chybný vstup. Posloupnost je prázdná.");
//     rl.close();
//     return;
//   }

//   if (sequence.length > 2000) {
//     console.log("Chybný vstup. Posloupnost je příliš dlouhá.");
//     rl.close();
//     return;
//   }

//   const pairCount = calculateSumPairs(sequence);
//   console.log(`Počet dvojic intervalů se stejným součtem: ${pairCount}`);

//   rl.close();
// }

// main();
