import React from 'react';
import DataTable from '../components/DataTable';

const columns = ['ID', 'Farmer', 'Worker', 'Amount', 'Commission', 'Status', 'Date'];

const transactions = [
  { ID: 'PAY-001', Farmer: 'Ramesh Patil', Worker: 'Suresh Kumar', Amount: '₹450', Commission: '₹33.75', Status: '✅ RELEASED', Date: '2026-03-12' },
  { ID: 'PAY-002', Farmer: 'Vijay Singh', Worker: 'Anjali Devi', Amount: '₹380', Commission: '₹28.50', Status: '🔒 HELD', Date: '2026-03-11' },
  { ID: 'PAY-003', Farmer: 'Anand Patil', Worker: 'Ravi Yadav', Amount: '₹420', Commission: '₹31.50', Status: '⏳ PENDING', Date: '2026-03-10' },
];

export default function Transactions() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Transactions</h1>
      <DataTable columns={columns} data={transactions} />
    </div>
  );
}
