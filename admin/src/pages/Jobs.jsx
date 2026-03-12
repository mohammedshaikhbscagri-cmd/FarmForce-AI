import React from 'react';
import DataTable from '../components/DataTable';

const columns = ['Title', 'Farmer', 'Workers', 'Wage/Day', 'Status', 'Date', 'Actions'];

const jobs = [
  { Title: 'Wheat Harvesting', Farmer: 'Ramesh Patil', Workers: '5/8', 'Wage/Day': '₹450', Status: '🟢 OPEN', Date: '2026-03-15', Actions: 'View' },
  { Title: 'Cotton Picking', Farmer: 'Vijay Singh', Workers: '10/10', 'Wage/Day': '₹380', Status: '🔵 IN_PROGRESS', Date: '2026-03-10', Actions: 'View' },
  { Title: 'Grape Pruning', Farmer: 'Anand Patil', Workers: '0/4', 'Wage/Day': '₹420', Status: '🟡 DRAFT', Date: '2026-03-20', Actions: 'View' },
];

export default function Jobs() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Jobs</h1>
      <DataTable columns={columns} data={jobs} />
    </div>
  );
}
