'use strict';

const fs = require('fs').promises;

// Antipattern: Hard code
(async () => {
  const data = await fs.readFile('./2-hard-code.js', 'utf8');
  const lines = data.split('\n');
  const str = lines[6];
  const fileName = str.substring(34, 50);
  console.dir({ fileName });
})();

// Solution
(async () => {

  const LINE_SEPARATOR = '\n';
  const FILE_ENCODING = 'utf8';

  const readFileBlock = async (name, line, start, end) => {
    const data = await fs.readFile(name, FILE_ENCODING);
    const lines = data.split(LINE_SEPARATOR);
    const str = lines[line];
    return str.substring(start, end);
  };

  const block = await readFileBlock('./2-hard-code.js', 6, 34, 50);
  console.dir({ block });
})();
