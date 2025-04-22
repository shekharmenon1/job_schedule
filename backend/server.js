const express = require('express');
const { exec } = require('child_process');
const cors = require('cors');
const path = require('path');
const app = express();
const PORT = 3000;
app.use(cors());
app.get('/', (req, res) => {
  // Run app.py using python
  exec('python3 app.py', { cwd: __dirname }, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return res.status(500).send(`Error running Python script`);
    }
    if (stderr) {
      console.error(`stderr: ${stderr}`);
    }
    res.send(stdout.trim());
  });
});
app.listen(PORT, () => {
  console.log(`Node server is running at http://localhost:${PORT}`);
});