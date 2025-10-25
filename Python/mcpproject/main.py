from fastmcp import FastMCP
from dotenv import load_dotenv
import json
import os
from datetime import datetime

load_dotenv()

mcp = FastMCP(name="Notes App")

# Simple in-memory storage (you can later replace with a database)
notes = []

@mcp.tool()
def get_all_notes() -> str:
    """Get all notes for the user"""
    if not notes:
        return "No notes found"
    
    result = "Your notes:\n"
    for i, note in enumerate(notes, 1):
        result += f"{i}. {note['content']} (Created: {note['created_at']})\n"
    return result

@mcp.tool()
def add_note(content: str) -> str:
    """Add a new note"""
    note = {
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id": len(notes) + 1
    }
    notes.append(note)
    return f"Note added successfully! Total notes: {len(notes)}"

@mcp.tool()
def delete_note(note_id: int) -> str:
    """Delete a note by ID"""
    if 1 <= note_id <= len(notes):
        deleted_note = notes.pop(note_id - 1)
        # Re-index remaining notes
        for i, note in enumerate(notes):
            note['id'] = i + 1
        return f"Deleted note: '{deleted_note['content']}'"
    return f"Note with ID {note_id} not found"

@mcp.tool()
def search_notes(keyword: str) -> str:
    """Search notes by keyword"""
    matching_notes = [note for note in notes if keyword.lower() in note['content'].lower()]
    
    if not matching_notes:
        return f"No notes found containing '{keyword}'"
    
    result = f"Notes containing '{keyword}':\n"
    for note in matching_notes:
        result += f"- {note['content']} (ID: {note['id']})\n"
    return result

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=8000
    )