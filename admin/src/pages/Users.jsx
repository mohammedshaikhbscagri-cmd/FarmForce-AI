import React from 'react';
import DataTable from '../components/DataTable';

const columns = ['Name', 'Phone', 'Role', 'District', 'Rating', 'Jobs', 'Verified', 'Actions'];

const users = [
  { Name: 'Ramesh Patil', Phone: '+91 9876543210', Role: 'Farmer', District: 'Pune', Rating: '4.5 ⭐', Jobs: 12, Verified: '✅', Actions: 'View' },
  { Name: 'Suresh Kumar', Phone: '+91 9765432109', Role: 'Worker', District: 'Nashik', Rating: '4.2 ⭐', Jobs: 34, Verified: '✅', Actions: 'View' },
  { Name: 'Anjali Devi', Phone: '+91 9654321098', Role: 'Worker', District: 'Solapur', Rating: '3.8 ⭐', Jobs: 18, Verified: '❌', Actions: 'View' },
];

export default function Users() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Users</h1>
      <DataTable columns={columns} data={users} />
    </div>
  );
}
