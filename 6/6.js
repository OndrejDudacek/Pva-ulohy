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
let inRack = false;
let itemsArray = [];
for (const shopingList of input) {
  for (const item of shopingList) {
    for (const rackIndex in racks) {
      for (const rackItem of racks[rackIndex]) {
        if (
          item.toLowerCase() === rackItem.toLowerCase() ||
          rackItem.toLowerCase().includes(item.toLowerCase())
        ) {
          itemsArray.push({
            shopingList: input.indexOf(shopingList),
            rack: rackIndex,
            originalName: item,
            rackName: rackItem,
          });
          inRack = true;
        }
      }
    }
    if (!inRack) {
      itemsArray.push({
        shopingList: input.indexOf(shopingList),
        rack: "",
        originalName: item,
        rackName: "N/A",
      });
    }
  }
}
itemsArray.sort((a, b) => a.rack - b.rack);

for (const shopingListIndex in input) {
  console.log("Optimalizovany seznam:");
  let optimaizedItemIndex = 0;
  for (const object of itemsArray) {
    if (object.shopingList == shopingListIndex) {
      console.log(
        ` ${optimaizedItemIndex}. ${object.originalName} -> #${object.rack} ${object.rackName}`
      );
      optimaizedItemIndex++;
    }
  }
}
