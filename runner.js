const { Interpreter } = require('tagscript');
const fs = require('fs');

const interpreter = new Interpreter();
const fileContent = fs.readFileSync(process.argv[2], 'utf-8');

interpreter.run(fileContent).then((result) => {
    console.log("Output:");
    console.log(result.body);
}).catch((error) => {
    console.error("Error executing tagscript:", error);
});
