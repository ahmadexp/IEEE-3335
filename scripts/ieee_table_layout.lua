-- Give standards tables stable, wrapping column widths in the PDF output.
local widths_by_column_count = {
  [2] = { 0.24, 0.76 },
  [3] = { 0.22, 0.32, 0.46 },
  [4] = { 0.16, 0.19, 0.325, 0.325 },
  [5] = { 0.27, 0.075, 0.115, 0.09, 0.45 },
}

function Table(table_element)
  local widths = widths_by_column_count[#table_element.colspecs]
  if widths == nil then
    return nil
  end

  local heading = table_element.head.rows[1]
  if heading ~= nil then
    local first_label = pandoc.utils.stringify(heading.cells[1].contents)
    if #table_element.colspecs == 2 and first_label == "Field" then
      widths = { 0.44, 0.56 }
    elseif #table_element.colspecs == 2 and first_label == "Profile and clause" then
      widths = { 0.40, 0.60 }
    elseif #table_element.colspecs == 4 and first_label == "P3335 concept" then
      widths = { 0.20, 0.27, 0.27, 0.26 }
    end
  end

  for index, column_spec in ipairs(table_element.colspecs) do
    table_element.colspecs[index] = { column_spec[1], widths[index] }
  end

  return table_element
end

-- Long tables can otherwise leave their section heading on the preceding page.
function Blocks(blocks)
  if not FORMAT:match("latex") then
    return nil
  end

  local result = pandoc.List()
  for index, block in ipairs(blocks) do
    local following = blocks[index + 1]
    local after_intro = blocks[index + 2]
    local table_follows = following ~= nil and (
      following.t == "Table" or (
        following.t == "Para" and after_intro ~= nil and after_intro.t == "Table"
      )
    )
    if block.t == "Header" and table_follows then
      result:insert(pandoc.RawBlock("latex", "\\Needspace{12\\baselineskip}"))
    end
    result:insert(block)
  end
  return result
end
