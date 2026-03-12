import React from 'react';
import StatsCard from '../components/StatsCard';
import DataTable from '../components/DataTable';
import {
  BarChart, Bar, LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
} from 'recharts';

const monthlyData = [
  { month: 'Oct', jobs: 120, workers: 340, revenue: 45000 },
  { month: 'Nov', jobs: 180, workers: 520, revenue: 72000 },
  { month: 'Dec', jobs: 240, workers: 680, revenue: 96000 },
  { month: 'Jan', jobs: 310, workers: 890, revenue: 124000 },
  { month: 'Feb', jobs: 290, workers: 820, revenue: 116000 },
  { month: 'Mar', jobs: 420, workers: 1100, revenue: 168000 },
];

export default function Dashboard() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold text-gray-800 mb-6">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <StatsCard title="Total Users" value="14,230" change="+12%" icon="👥" />
        <StatsCard title="Active Jobs" value="342" change="+8%" icon="💼" />
        <StatsCard title="GMV (₹)" value="₹12.4L" change="+23%" icon="💰" />
        <StatsCard title="Revenue (₹)" value="₹93K" change="+23%" icon="📈" />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="text-lg font-semibold mb-4">Monthly Job Postings</h2>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={monthlyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="jobs" fill="#2E7D32" name="Jobs Posted" />
              <Bar dataKey="workers" fill="#F9A825" name="Workers Hired" />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="bg-white rounded-lg shadow p-4">
          <h2 className="text-lg font-semibold mb-4">Revenue Trend (₹)</h2>
          <ResponsiveContainer width="100%" height={250}>
            <LineChart data={monthlyData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Line type="monotone" dataKey="revenue" stroke="#2E7D32" strokeWidth={2} name="Revenue" />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
