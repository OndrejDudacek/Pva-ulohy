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

const calculateDistances = (planes) => {
  let results = {};
  for (let first = 0; first < planes.length; first++) {
    for (let second = first + 1; second < planes.length; second++) {
      const distance =
        Math.round(
          Math.sqrt(
            (planes[first][0][0] - planes[second][0][0]) ** 2 +
              (planes[first][0][1] - planes[second][0][1]) ** 2
          ) * 1000000
        ) / 1000000;
      //console.log(distance);
      results[`${planes[first][1]} - ${planes[second][1]}`] = distance;
    }
  }
  return results;
};

findInputsAndOutputs();
for (const inputIndex in inputs) {
  let running = true;
  console.log(inputs[inputIndex]);
  const [input, expectedOutput] = readInputAndOutput(
    inputs[inputIndex],
    outputs[inputIndex]
  );
  let planes = input.split("\n");
  for (const i in planes) {
    if (
      !planes[i].includes(":") ||
      !planes[i].includes(",") ||
      planes.length < 2
    ) {
      console.log(expectedOutput + "\n---");
      console.log(`Pozice letadel:\nNesprávný vstup.`);
      console.log("\n-------------------------------------------\n");
      running = false;
      break;
    }

    planes[i] = planes[i].split(": ");
    planes[i][0] = planes[i][0].split(",");
    planes[i][0] = planes[i][0].map((x) => parseFloat(x));

    if (planes[i].length !== 2) {
      console.log(expectedOutput + "\n---");
      console.log(`Pozice letadel:\nNesprávný vstup.`);
      console.log("\n-------------------------------------------\n");
      running = false;
      break;
    }
  }
  if (!running) {
    continue;
  }
  let distances = calculateDistances(planes);
  let smallestDistance = Number.MAX_SAFE_INTEGER;
  for (const distance in distances) {
    if (distances[distance] < smallestDistance) {
      smallestDistance = distances[distance];
    }
  }
  for (const planes in distances) {
    if (distances[planes] !== smallestDistance) {
      delete distances[planes];
    }
  }
  console.log(expectedOutput + "\n---");
  console.log(`Pozice letadel:
Vzdalenost nejblizsich letadel: ${smallestDistance}
Nalezenych dvojic: ${Object.keys(distances).length}`);
  for (const keys in distances) {
    console.log(keys);
  }
  console.log("\n-------------------------------------------\n");
}
