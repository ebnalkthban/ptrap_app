import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/part.dart'; // تأكد من وجود ملف المودل في مجلد models

class DatabaseHelper {
  static final DatabaseHelper instance = DatabaseHelper._init();
  static Database? _database;

  DatabaseHelper._init();

  Future<Database> get database async {
    if (_database != null) return _database!;
    _database = await _initDB('phone_parts.db');
    return _database!;
  }

  Future<Database> _initDB(String filePath) async {
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, filePath);

    return await openDatabase(
      path,
      version: 1,
      onCreate: _createDB,
    );
  }

  Future _createDB(Database db, int version) async {
    await db.execute('''
      CREATE TABLE parts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        barcode TEXT,
        quantity INTEGER NOT NULL
      )
    ''');
  }

  // العمليات الأساسية (CRUD)
  Future<int> insertPart(Part part) async {
    final db = await instance.database;
    return await db.insert('parts', part.toMap());
  }

  Future<List<Part>> getAllParts() async {
    final db = await instance.database;
    final result = await db.query('parts');
    return result.map((json) => Part.fromMap(json)).toList();
  }

  Future<int> updatePart(Part part) async {
    final db = await instance.database;
    return await db.update(
      'parts',
      part.toMap(),
      where: 'id = ?',
      whereArgs: [part.id],
    );
  }

  Future<int> deletePart(int id) async {
    final db = await instance.database;
    return await db.delete(
      'parts',
      where: 'id = ?',
      whereArgs: [id],
    );
  }

  Future close() async {
    final db = await instance.database;
    db.close();
  }
}