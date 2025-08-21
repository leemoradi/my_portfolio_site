// Global variables for charts
let committeeActivityChart, committeeTypesChart;

// Fetch and display data
async function loadDashboard() {
    try {
        // Load committee data first (primary focus)
        const committeeResponse = await fetch('../data/committee_data.json');
        const committeeData = await committeeResponse.json();
        
        // Load bill data second
        const billResponse = await fetch('../data/latest_bills.json');
        const billData = await billResponse.json();
        
        // Update committee statistics first
        updateCommitteeStats(committeeData);
        
        // Update bill statistics
        updateBillStats(billData);
        
        // Create committee charts (primary focus)
        createCommitteeCharts(committeeData);
        
    } catch (error) {
        console.error('Error loading dashboard:', error);
        document.body.innerHTML += `<p style="color: red;">❌ Error: ${error.message}</p>`;
    }
}

function updateCommitteeStats(data) {
    const summary = data.summary || {};
    document.getElementById('totalCommittees').textContent = summary.total_committees || 0;
    document.getElementById('houseCommittees').textContent = summary.house_committees || 0;
    document.getElementById('senateCommittees').textContent = summary.senate_committees || 0;
}

function updateBillStats(data) {
    document.getElementById('totalBills').textContent = data.total_bills || 0;

    // Update date range
    const dateRange = data.date_range;
    if (dateRange && dateRange.from && dateRange.to) {
        document.getElementById('dateRange').textContent = 
            `Committee analysis data from ${dateRange.from} to ${dateRange.to}`;
    }
}

function createCommitteeCharts(data) {
    const committees = data.committees || {};
    const committeeTypes = data.committee_types || {};
    
    // Create Committee Activity Chart
    const activityCtx = document.getElementById('committeeActivityChart');
    if (activityCtx) {
        // Get top 10 committees by bill count
        const sortedCommittees = Object.entries(committees)
            .sort(([,a], [,b]) => b.bill_count - a.bill_count)
            .slice(0, 10);
        
        const committeeNames = sortedCommittees.map(([name]) => name);
        const billCounts = sortedCommittees.map(([, data]) => data.bill_count);
        
        committeeActivityChart = new Chart(activityCtx, {
            type: 'bar',
      data: {
                labels: committeeNames,
        datasets: [{
                    label: 'Bill Count',
                    data: billCounts,
                    backgroundColor: 'rgba(54, 162, 235, 0.8)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
        }]
      },
      options: {
        responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: false
                    },
                    title: {
                        display: true,
                        text: 'Top 10 Most Active Committees'
                    }
                },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
                            text: 'Number of Bills'
                        },
                        ticks: {
                            stepSize: 5
            }
          }
        }
      }
    });
    }
    
    // Create Committee Types Chart
    const typesCtx = document.getElementById('committeeTypesChart');
    if (typesCtx) {
        const typeLabels = Object.keys(committeeTypes);
        const typeCounts = Object.values(committeeTypes);
        
        committeeTypesChart = new Chart(typesCtx, {
            type: 'pie',
            data: {
                labels: typeLabels,
                datasets: [{
                    data: typeCounts,
                    backgroundColor: [
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                        'rgba(75, 192, 192, 0.8)',
                        'rgba(153, 102, 255, 0.8)'
                    ],
                    borderColor: [
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 99, 132, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)'
                    ],
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom'
                    },
                    title: {
                        display: true,
                        text: 'Committee Types Distribution'
                    }
                }
            }
        });
    }
}

// Load dashboard when page loads
document.addEventListener('DOMContentLoaded', loadDashboard);



