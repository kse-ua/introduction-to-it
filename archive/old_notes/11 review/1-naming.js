'use strict';

// Antipattern: Short identifiers
{
  const n = 'Marcus Aurelius';
}

// Antipattern: Long identifiers
{
  const romanEmperorAndOutstandingThinker = 'Marcus Aurelius';
}

// Antipattern: Same name but different meaning
{
  const name = 'Marcus Aurelius';
  if (name) {
    const name = './config.js';
    console.dir({ name });
  }
}

// Antipattern: Same meaning but different naming
{
  const fileName = './config.js';
  if (!fileName) {
    const file = './backup/config.js';
    if (!file) {
      const filePath = '../config.js';
      console.dir({ filePath });
    }
  }
}

// Antipattern: Inconsistent names
{
  const api = {
    setPort: () => {},
    assignAddress: () => {},
    definePath: () => {},
  };
  console.dir({ api });
}

// Antipattern: Non descriptive names
{
  class ApplicationController {
    constructor(link) {
      this.link = link;
    }

    execute(handler) {
      this.link(handler);
    }
  }
}
