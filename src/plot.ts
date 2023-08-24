import { Chart } from 'chart.js'

// Sample data
const data = {
  labels: ['2023-01', '2023-02', '2023-03'], // Months as labels
  distance: [10, 15, 12], // Distance values
  avgSpeed: [5.0, 5.5, 6.0], // Average speed values
  activityCounts: [8, 10, 6] // Activity counts per month
}

// Bar Plot for Activities Over Time
const ctxActivities = document.getElementById('activities-chart') as HTMLCanvasElement

/* eslint-disable no-new */
new Chart(ctxActivities, {
  type: 'bar',
  data: {
    labels: data.labels,
    datasets: [{
      label: 'Activity Counts',
      data: data.activityCounts,
      backgroundColor: 'rgba(75, 192, 192, 0.6)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
    }],
  },
  options: {
    scales: {
      x: { type: 'category' as const },
      y: { beginAtZero: true },
    },
    plugins: {
      title: { display: true, text: 'Number of Activities per Month' },
    },
  },
})

// Line Plot for Average Speed Over Time
const ctxAvgSpeed = document.getElementById('avg-speed-chart') as HTMLCanvasElement

new Chart(ctxAvgSpeed, {
  type: 'line',
  data: {
    labels: data.labels,
    datasets: [{
      label: 'Average Speed',
      data: data.avgSpeed,
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 2,
      fill: false,
    }],
  },
  options: {
    scales: {
      x: { type: 'category' as const },
      y: { beginAtZero: true },
    },
    plugins: {
      title: { display: true, text: 'Average Speed Over Time' },
    },
  },
})
