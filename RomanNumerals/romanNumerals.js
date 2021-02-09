const NUMERAL = "774";

const numerals = [
  { number: 1000, value: "M" },
  { number: 900, value: "CM" },
  { number: 500, value: "D" },
  { number: 400, value: "CD" },
  { number: 100, value: "C" },
  { number: 90, value: "XC" },
  { number: 50, value: "L" },
  { number: 40, value: "XL" },
  { number: 10, value: "X" },
  { number: 9, value: "IX" },
  { number: 5, value: "V" },
  { number: 4, value: "IV" },
  { number: 1, value: "I" },
];

const toNumeral = (roman) => {
  var result = 0;
  while (roman.length > 0) {
    try {
      const currentNumeral = numerals.filter((num) => {
        return num.value === roman.slice(0, num.value.length);
      })[0];
      result += currentNumeral.number;
      roman = roman.slice(currentNumeral.value.length);
    } catch (e) {
      console.log("Non Romanial Numeral!");
      return;
    }
  }
  return result;
};

const toRoman = (numeral) => {
  var result = "";
  while (numeral > 0) {
    let { number, value } = numerals.filter((num) => {
      return numeral / num.number >= 1.0;
    })[0];

    numeral -= number;
    result += value;
  }
  return result;
};
console.log(
  `${NUMERAL} in Roman Numerals is: ${toRoman(
    NUMERAL
  )} and converted back: ${toNumeral(toRoman(NUMERAL))}`
);
