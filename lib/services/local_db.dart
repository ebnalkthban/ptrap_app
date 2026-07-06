import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/part.dart';

class LocalDB {
  static Database? _database;

  static Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB();
    return _database!;
  }

  static Future<Database> _initDB() async {
    String path = join(await getDatabasesPath(), 'parts.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE parts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            barcode TEXT,
            quantity INTEGER NOT NULL
          )
        ''');
      },
    );
  }

  static Future<int> insertPart(Part part) async {
    final db = await database;
    return await db.insert('parts', part.toMap());
  }

  static Future<List<Part>> getAllParts() async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query('parts');
    return List.generate(maps.length, (i) => Part.fromMap(maps[i]));
  }

  static Future<List<Part>> searchParts(String query) async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query(
      'parts',
      where: 'name LIKE ? OR barcode LIKE ?',
      whereArgs: ['%$query%', '%$query%'],
    );
    return List.generate(maps.length, (i) => Part.fromMap(maps[i]));
  }

  static Future<int> updatePart(Part part) async {
    final db = await database;
    return await db.update('parts', part.toMap(), where: 'id = ?', whereArgs: [part.id]);
  }

  static Future<int> deletePart(int id) async {
    final db = await database;
    return await db.delete('parts', where: 'id = ?', whereArgs: [id]);
  }

  static Future<Part?> getPartByBarcode(String barcode) async {
    final db = await database;
    final List<Map<String, dynamic>> maps = await db.query(
      'parts',
      where: 'barcode = ?',
      whereArgs: [barcode],
    );
    if (maps.isNotEmpty) return Part.fromMap(maps.first);
    return null;
  }
}