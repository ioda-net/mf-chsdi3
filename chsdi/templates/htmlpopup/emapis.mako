<%inherit file="base.mako"/>

<%def name="table_body(c, lang)">
  <tr><td class="cell-left">featureId</td>     <td>${c['featureId'] or '-'}</td></tr>
  <tr><td class="cell-left">geschaeftsnummer</td>     <td>${c['attributes']['geschaeftsnummer'] or '-'}</td></tr>
  <tr><td class="cell-left">typ</td>     <td>${c['attributes']['typ'] or '-'}</td></tr>
</%def>
