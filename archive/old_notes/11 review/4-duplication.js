'use strict';

const { promises, watch } = require('fs');
const { readFile, readdir } = promises;
const fs = { watch, readFile, readdir };

// Antipattern: Duplicated code
{
  const cache = new Map();

  const watchFolder = (path) => {
    fs.watch(path, async (event, file) => {
      try {
        const data = await fs.readFile(file, 'utf8');
        cache.set(file, data);
      } catch (err) {
        cache.delete(file);
      }
    });
  };

  const cacheFolder = async (path) => {
    watchFolder(path);
    const files = await fs.readdir(path);
    for (const file of files) {
      try {
        const data = fs.readFile(file, 'utf8');
        cache.set(file, data);
      } catch (err) {
        cache.delete(file);
      }
    }
  };

  cacheFolder('./');
}

// Refactored
{
  const cache = new Map();

  const cacheFile = async (file) => {
    try {
      const data = await fs.readFile(file, 'utf8');
      cache.set(file, data);
    } catch (err) {
      cache.delete(file);
    }
  };

  const watchFolder = (path) => {
    fs.watch(path, (event, file) => {
      cacheFile(file);
    });
  };

  const cacheFolder = async (path) => {
    watchFolder(path);
    const files = await fs.readdir(path);
    for (const file of files) cacheFile(file);
  };

  cacheFolder('./');
}
