import React from 'react';

export default function StatsCard({ title, value, change, icon }) {
  const isPositive = change?.startsWith('+');
  return (
    <div className="bg-white rounded-lg shadow p-5 flex items-center gap-4">
      <div className="text-4xl">{icon}</div>
      <div>
        <div className="text-gray-500 text-sm">{title}</div>
        <div className="text-2xl font-bold text-gray-800">{value}</div>
        {change && (
          <div className={`text-sm font-medium ${isPositive ? 'text-green-600' : 'text-red-600'}`}>
            {change} vs last month
          </div>
        )}
      </div>
    </div>
  );
}
