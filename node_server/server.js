const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
app.use(bodyParser.json());

mongoose.connect('mongodb://localhost:27017/mydatabase', { useNewUrlParser: true, useUnifiedTopology: true });

const DataSchema = new mongoose.Schema({
    dataField: String
});

const Data = mongoose.model('Data', DataSchema);

app.post('/api/data', (req, res) => {
    const newData = new Data({ dataField: req.body.dataField });
    newData.save().then(() => res.sendStatus(200));
});

app.get('/api/data', (req, res) => {
    Data.find().then(data => res.json(data));
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
