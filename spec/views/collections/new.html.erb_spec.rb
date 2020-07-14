require 'rails_helper'

RSpec.describe "collections/new", type: :view do
  before(:each) do
    assign(:collection, Collection.new(
      name: "MyString",
      unlocked: false,
      note: "MyText"
    ))
  end

  it "renders new collection form" do
    render

    assert_select "form[action=?][method=?]", collections_path, "post" do

      assert_select "input[name=?]", "collection[name]"

      assert_select "input[name=?]", "collection[unlocked]"

      assert_select "textarea[name=?]", "collection[note]"
    end
  end
end
