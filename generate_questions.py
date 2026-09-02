#!/usr/bin/env python3
"""Fetch LeetCode problems and generate markdown files."""

import json
import re
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

PROBLEMS = [
    "Two Sum",
    "Contains Duplicate",
    "Valid Anagram",
    "Group Anagrams",
    "Top K Frequent Elements",
    "Product of Array Except Self",
    "Longest Consecutive Sequence",
    "Subarray Sum Equals K",
    "Valid Palindrome",
    "Two Sum II - Input Array Is Sorted",
    "3Sum",
    "Container With Most Water",
    "Trapping Rain Water",
    "Best Time to Buy and Sell Stock",
    "Longest Substring Without Repeating Characters",
    "Longest Repeating Character Replacement",
    "Permutation in String",
    "Minimum Window Substring",
    "Sliding Window Maximum",
    "Valid Parentheses",
    "Min Stack",
    "Evaluate Reverse Polish Notation",
    "Daily Temperatures",
    "Car Fleet",
    "Largest Rectangle in Histogram",
    "Binary Search",
    "Search a 2D Matrix",
    "Koko Eating Bananas",
    "Find Minimum in Rotated Sorted Array",
    "Search in Rotated Sorted Array",
    "Time Based Key-Value Store",
    "Median of Two Sorted Arrays",
    "Reverse Linked List",
    "Merge Two Sorted Lists",
    "Linked List Cycle",
    "Reorder List",
    "Remove Nth Node From End of List",
    "Copy List with Random Pointer",
    "Add Two Numbers",
    "LRU Cache",
    "Invert Binary Tree",
    "Maximum Depth of Binary Tree",
    "Diameter of Binary Tree",
    "Balanced Binary Tree",
    "Same Tree",
    "Subtree of Another Tree",
    "Binary Tree Level Order Traversal",
    "Binary Tree Right Side View",
    "Count Good Nodes in Binary Tree",
    "Validate Binary Search Tree",
    "Kth Smallest Element in a BST",
    "Construct Binary Tree from Preorder and Inorder Traversal",
    "Binary Tree Maximum Path Sum",
    "Serialize and Deserialize Binary Tree",
    "Kth Largest Element in an Array",
    "K Closest Points to Origin",
    "Task Scheduler",
    "Find Median from Data Stream",
    "Merge Intervals",
    "Insert Interval",
    "Non-overlapping Intervals",
    "Meeting Rooms II",
    "Jump Game",
    "Jump Game II",
    "Gas Station",
    "Subsets",
    "Combination Sum",
    "Permutations",
    "Subsets II",
    "Combination Sum II",
    "Word Search",
    "Palindrome Partitioning",
    "N-Queens",
    "Number of Islands",
    "Clone Graph",
    "Max Area of Island",
    "Rotting Oranges",
    "Pacific Atlantic Water Flow",
    "Surrounded Regions",
    "Course Schedule",
    "Course Schedule II",
    "Graph Valid Tree",
    "Number of Connected Components in an Undirected Graph",
    "Word Ladder",
    "Network Delay Time",
    "Min Cost to Connect All Points",
    "Cheapest Flights Within K Stops",
    "Alien Dictionary",
    "Climbing Stairs",
    "House Robber",
    "House Robber II",
    "Coin Change",
    "Longest Increasing Subsequence",
    "Word Break",
    "Partition Equal Subset Sum",
    "Unique Paths",
    "Longest Common Subsequence",
    "Coin Change II",
    "Edit Distance",
    "Longest Palindromic Subsequence",
    "Implement Trie (Prefix Tree)",
    "Design Add and Search Words Data Structure",
    "Word Search II",
    "Single Number",
    "Number of 1 Bits",
    "Counting Bits",
    "Reverse Bits",
    "Missing Number",
    "Sum of Two Integers",
    "Redundant Connection",
    "Swim in Rising Water",
    "Burst Balloons",
    "Distinct Subsequences",
    "Interleaving String",
]


class HTMLToMarkdown(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.in_pre = False
        self.in_code = False

    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.in_pre = True
            self.parts.append("\n\n```\n")
        elif tag == "code":
            self.in_code = True
            if not self.in_pre:
                self.parts.append("`")
        elif tag == "p":
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "strong":
            self.parts.append("**")
        elif tag == "em":
            self.parts.append("*")
        elif tag in ("ul", "ol"):
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag == "pre":
            self.in_pre = False
            self.parts.append("\n```\n")
        elif tag == "code":
            self.in_code = False
            if not self.in_pre:
                self.parts.append("`")
        elif tag == "strong":
            self.parts.append("**")
        elif tag == "em":
            self.parts.append("*")

    def handle_data(self, data):
        self.parts.append(data)

    def get_text(self):
        text = "".join(self.parts)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip()


def fetch_url(url, data=None, retries=3):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (compatible; dsa-prep/1.0)",
    }
    for attempt in range(retries):
        try:
            if data:
                req = urllib.request.Request(
                    url, data=json.dumps(data).encode(), headers=headers
                )
            else:
                req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 403 and attempt < retries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            raise


def load_slug_map():
    data = json.loads(fetch_url("https://leetcode.com/api/problems/all/"))
    slug_map = {}
    for p in data["stat_status_pairs"]:
        title = p["stat"]["question__title"]
        slug = p["stat"]["question__title_slug"]
        slug_map[title.lower()] = slug
    return slug_map


def html_to_markdown(html):
    parser = HTMLToMarkdown()
    parser.feed(html)
    return parser.get_text()


def fetch_problem(slug):
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        content
        difficulty
        isPaidOnly
      }
    }
    """
    raw = fetch_url(
        "https://leetcode.com/graphql",
        {"query": query, "variables": {"titleSlug": slug}},
    )
    return json.loads(raw).get("data", {}).get("question")


def main():
    slug_map = load_slug_map()
    out_dir = Path(__file__).parent / "questions"
    out_dir.mkdir(exist_ok=True)

    failed = []
    skipped_premium = []
    for title in PROBLEMS:
        slug = slug_map.get(title.lower())
        if not slug:
            failed.append(title)
            print(f"MISSING SLUG: {title}")
            continue

        print(f"Fetching: {title} ({slug})")
        problem = fetch_problem(slug)
        if not problem:
            failed.append(title)
            print(f"FAILED FETCH: {title}")
            continue

        if problem.get("isPaidOnly") or not problem.get("content"):
            skipped_premium.append(title)
            print(f"SKIPPED PREMIUM: {title}")
            continue

        content_md = html_to_markdown(problem["content"])

        md = f"""# {problem['title']}

**Difficulty:** {problem['difficulty']}
**LeetCode:** https://leetcode.com/problems/{slug}/

## Problem

{content_md}
"""
        filepath = out_dir / f"{slug}.md"
        filepath.write_text(md, encoding="utf-8")
        time.sleep(0.5)

    print(f"\nDone. Created {len(list(out_dir.glob('*.md')))} files.")
    if skipped_premium:
        print(f"Skipped premium ({len(skipped_premium)}): {skipped_premium}")
    if failed:
        print(f"Failed ({len(failed)}): {failed}")


if __name__ == "__main__":
    main()
