import * as fs from 'fs';
import * as Papa from 'papaparse';

const csvFilePath = 'data/activities.csv';
const csvData = fs.readFileSync(csvFilePath, 'utf8');

const parsedData = Papa.parse(csvData, { header: true });
const activities = parsedData.data;

const totalDistance = activities.reduce((sum, activity) => sum + parseFloat(activity.Distance), 0);
const averageSpeed = activities.reduce((sum, activity) => sum + parseFloat(activity['Average Speed']), 0) / activities.length;

console.log(`totalDistance: ${totalDistance}`)
console.log(`averageSpeed: ${averageSpeed}`)
