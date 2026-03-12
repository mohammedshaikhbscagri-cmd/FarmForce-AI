import 'package:flutter/material.dart';

final ThemeData farmForceTheme = ThemeData(
  useMaterial3: true,
  colorScheme: ColorScheme.fromSeed(
    seedColor: const Color(0xFF2E7D32),
    primary: const Color(0xFF2E7D32),
    secondary: const Color(0xFFF9A825),
  ),
  appBarTheme: const AppBarTheme(
    backgroundColor: Color(0xFF2E7D32),
    foregroundColor: Colors.white,
    elevation: 2,
  ),
  elevatedButtonTheme: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: const Color(0xFF2E7D32),
      foregroundColor: Colors.white,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(8)),
      padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
    ),
  ),
  cardTheme: CardTheme(
    elevation: 3,
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
    margin: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
  ),
  textTheme: const TextTheme(
    headlineLarge: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Color(0xFF1B5E20)),
    headlineMedium: TextStyle(fontSize: 22, fontWeight: FontWeight.w600, color: Color(0xFF2E7D32)),
    bodyLarge: TextStyle(fontSize: 16, color: Color(0xFF212121)),
    bodyMedium: TextStyle(fontSize: 14, color: Color(0xFF424242)),
  ),
);
