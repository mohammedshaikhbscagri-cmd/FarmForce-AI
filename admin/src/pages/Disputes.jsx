import React from 'react';
import DataTable from '../components/DataTable';

const columns = ['ID', 'Type', 'Reporter', 'Status', 'Created', 'Actions'];

const disputes = [
  { ID: 'DIS-001', Type: 'Payment', Reporter: 'Suresh Kumar', Status: '🔴 OPEN', Created: '2026-03-10', Actions: 'Resolve' },
  { ID: 'DIS-002', Type: 'No Show', Reporter: 'Ramesh Patil', Status: '🟡 UNDER_REVIEW', Created: '2026-03-08', Actions: 'Resolve' },
  { ID: 'DIS-003', Type: 'Quality', Reporter: 'Vijay Singh', Status: '🟢 RESOLVED', Created: '2026-03-05', Actions: 'View' },
];

export default function Disputes() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Disputes</h1>
      <DataTable columns={columns} data={disputes} />
    </div>
  );
}
