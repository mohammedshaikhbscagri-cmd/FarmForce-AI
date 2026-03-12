import React from 'react';
import { NavLink } from 'react-router-dom';

const navItems = [
  { to: '/dashboard', label: 'Dashboard', icon: '📊' },
  { to: '/users', label: 'Users', icon: '👥' },
  { to: '/jobs', label: 'Jobs', icon: '💼' },
  { to: '/transactions', label: 'Transactions', icon: '💳' },
  { to: '/disputes', label: 'Disputes', icon: '⚖️' },
];

export default function Sidebar() {
  return (
    <div className="w-64 bg-green-800 text-white flex flex-col">
      <div className="p-6 border-b border-green-700">
        <div className="text-2xl mb-1">🌾</div>
        <div className="font-bold text-lg">FarmForce AI</div>
        <div className="text-green-300 text-sm">Admin Dashboard</div>
      </div>
      <nav className="flex-1 p-4">
        {navItems.map((item) => (
          <NavLink
            key={item.to}
            to={item.to}
            className={({ isActive }) =>
              `flex items-center gap-3 px-4 py-3 rounded-lg mb-1 transition-colors ${
                isActive ? 'bg-green-600 font-medium' : 'hover:bg-green-700'
              }`
            }
          >
            <span>{item.icon}</span>
            <span>{item.label}</span>
          </NavLink>
        ))}
      </nav>
      <div className="p-4 border-t border-green-700 text-sm text-green-300">
        FarmForce AI v1.0.0
      </div>
    </div>
  );
}
